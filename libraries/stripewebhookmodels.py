from nebriosmodels import NebriOSModel, NebriOSField, NebriOSReference


class Account(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Balance(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Bitcoin(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Charge(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Coupon(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Customer(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Invoice(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class InvoiceItem(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Plan(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Recipient(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Transfer(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    stripe_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)
