from nebrios_authentication_lib import token_required
from stripewebhookmodels import Account, Balance, Bitcoin, Charge, Coupon, Customer, Invoice,
                                InvoiceItem, Plan, Recipient, Transfer
import json


@token_required(realm='stripe')
def all_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type == 'account':
        event = Account()
    elif event_type == 'balance':
        event = Balance()
    elif event_type == 'bitcoin':
        event = Bitcoin()
    elif event_type == 'charge':
        event = Charge()
    elif event_type == 'coupon':
        event = Coupon()
    elif event_type == 'customer':
        event = Customer()
    elif event_type == 'invoice':
        event = Invoice()
    elif event_type == 'invoiceitem':
        event = InvoiceItem()
    elif event_type == 'plan':
        event = Plan()
    elif event_type == 'recipient':
        event = Recipient()
    elif event_type == 'transfer':
        event = Transfer()
    else:
        return HttpResponseBadRequest

    event.event_type = event_data['type'].split('.')[1]
    event.stripe_id = event_data['id']
    event.date_received = datetime.now()
    event.raw_data = event_data
    event.save()
    return {}


@token_required(realm='stripe')
def account_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'account':
        return HttpResponseBadRequest
    event = Account(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def balance_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'balance':
        return HttpResponseBadRequest
    event = Balance(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def bitcoin_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'bitcoin':
        return HttpResponseBadRequest
    event = Bitcoin(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def charge_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'charge':
        return HttpResponseBadRequest
    event = Charge(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def coupon_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'coupon':
        return HttpResponseBadRequest
    event = Coupon(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def customer_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'customer':
        return HttpResponseBadRequest
    event = Customer(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def invoice_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'invoice':
        return HttpResponseBadRequest
    event = Invoice(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def invoiceitem_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'invoiceitem':
        return HttpResponseBadRequest
    event = InvoiceItem(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def plan_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'plan':
        return HttpResponseBadRequest
    event = Plan(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def receipt_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'receipt':
        return HttpResponseBadRequest
    event = Receipt(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}


@token_required(realm='stripe')
def transfer_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['type'].split('.')[0]
    if event_type != 'transfer':
        return HttpResponseBadRequest
    event = Transfer(
        event_type=event_data['type'].split('.')[1]
        stripe_id=event_data['id']
        date_received=datetime.now()
        raw_data=event_data
    )
    event.save()
    return {}
