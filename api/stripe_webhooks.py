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
        try:
            event = Account.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Account()
    elif event_type == 'balance':
        try:
            event = Balance.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Balance()
    elif event_type == 'bitcoin':
        try:
            event = Bitcoin.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Bitcoin()
    elif event_type == 'charge':
        try:
            event = Charge.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Charge()
    elif event_type == 'coupon':
        try:
            event = Coupon.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Coupon()
    elif event_type == 'customer':
        try:
            event = Customer.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Customer()
    elif event_type == 'invoice':
        try:
            event = Invoice.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Invoice()
    elif event_type == 'invoiceitem':
        try:
            event = InvoiceItem.get(stripe_id=event_data['id'])
            return {}
        except:
            event = InvoiceItem()
    elif event_type == 'plan':
        try:
            event = Plan.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Plan()
    elif event_type == 'recipient':
        try:
            event = Recipient.get(stripe_id=event_data['id'])
            return {}
        except:
            event = Recipient()
    elif event_type == 'transfer':
        try:
            event = Transfer.get(stripe_id=event_data['id'])
            return {}
        except:
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
    try:
        event = Account.get(stripe_id=event_data['id'])
        return {}
    except:
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
    try:
        event = Balance.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Bitcoin.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Charge.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Coupon.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Customer.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Invoice.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = InvoiceItem.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Plan.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Receipt.get(stripe_id=event_data['id']
        return {}
    except:
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
    try:
        event = Transfer.get(stripe_id=event_data['id']
        return {}
    except:
        event = Transfer(
            event_type=event_data['type'].split('.')[1]
            stripe_id=event_data['id']
            date_received=datetime.now()
            raw_data=event_data
        )
        event.save()
        return {}
