import json

def extract_rates(data, params):
    rates = []

    for room_type in data.get('roomTypes', []):
        offers = room_type.get('offers', [])
        if offers and 'bedGroups' in offers[0] and offers[0]['bedGroups']:
            room_name = offers[0]['bedGroups'][0].get('description', '')
        else:
            room_name = ''
        
        for offer in offers:
            rate_name = offer.get('name')
            guests = int(params['adults']) + int(params['children']) + int(params['infants'])
            cancellation_policy = offer.get('cancellationPolicy', {}).get('description', '')
            price = offer.get('charges', {}).get('total', {}).get('amount', 0)
            currency = offer.get('charges', {}).get('total', {}).get('currency', 'AUD')
            top_deal = offer.get('memberDealAvailable', False)

            rates.append({
                "Room_name": room_name,
                "Rate_name": rate_name,
                "Number_of_Guests": guests,
                "Cancellation_Policy": cancellation_policy,
                "Price": float(price),
                "Top_Deal": top_deal,
                "Currency": currency
            })

    return rates