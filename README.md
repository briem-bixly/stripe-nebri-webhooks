# Stripe Nebri Webhooks

This app is intended for use in a NebriOS instance. Visit https://nebrios.com to sign up for free!

<h2>Installation</h2>
This app requires very little in terms of setup. Please ensure that all files are placed in the correct places over SFTP.

- `libraries/stripewebhookmodels.py` should be copied to /libraries
- `api/stripe_webhooks.py` should be copied to /api

<h2>Requirements</h2>
This app requires the use of https://github.com/briem-bixly/nebrios-authentication.

<h2>Usage</h2>
See https://nebrios.com/blog/web-hooks-nebri for a detailed example on how to set up webhooks with Nebri and Stripe.

<h2>Endpoints</h2>
- all_events: can be used for any event type
- account_events: for use with account events
- balance_events: for use with balance events
- bitcoin_events: for use with bitcoin events
- charge_events: for use with charge events
- coupon_events: for use with coupon events
- customer_events: for use with customer events
- invoice_events: for use with invoice events
- invoiceitem_events: for use with invoice item events
- plan_events: for use with plan events
- receipt_events: for use with receipt events
- transer_events: for use with transfer events

<strong>NOTE</strong>: if an endpoint is used for webhooks with a different event type, the webhook will fail and no object will be created.

<h2>Models</h2>
Models are named after events.
Currently supported events:
- account
- balance
- bitcoin
- charge
- coupon
- customer
- invoice
- invoiceitem
- plan
- receipt
- transfer

All models have the same fields:
- event_type: the type of event. i.e. if we get an event of charge.succeeded, this will be 'succeeded'.
- date_received: the datetime that we received the webhook event.
- stripe_id: the id that stripe provides for the event. can be used for debouncing purposes.
- raw_data: the json representation of the full request body

Sample request body:
```
{
  "created": 1326853478,
  "livemode": false,
  "id": "evt_00000000000000",
  "type": "charge.succeeded",
  "object": "event",
  "request": null,
  "pending_webhooks": 1,
  "api_version": "2015-09-08",
  "data": {
    "object": {
      "id": "ch_00000000000000",
      "object": "charge",
      "created": 1442251313,
      "livemode": false,
      "paid": true,
      "status": "succeeded",
      "amount": 100,
      "currency": "usd",
      "refunded": false,
      "source": {
        "id": "card_00000000000000",
        "object": "card",
        "last4": "4242",
        "brand": "Visa",
        "funding": "credit",
        "exp_month": 8,
        "exp_year": 2016,
        "country": "US",
        "name": null,
        "address_line1": null,
        "address_line2": null,
        "address_city": null,
        "address_state": null,
        "address_zip": null,
        "address_country": null,
        "cvc_check": null,
        "address_line1_check": null,
        "address_zip_check": null,
        "tokenization_method": null,
        "dynamic_last4": null,
        "metadata": {},
        "customer": null
      },
      "captured": true,
      "balance_transaction": "txn_00000000000000",
      "failure_message": null,
      "failure_code": null,
      "amount_refunded": 0,
      "customer": null,
      "invoice": null,
      "description": "My First Test Charge (created for API docs)",
      "dispute": null,
      "metadata": {},
      "statement_descriptor": null,
      "fraud_details": {},
      "receipt_email": null,
      "receipt_number": null,
      "shipping": null,
      "destination": null,
      "application_fee": null,
      "refunds": {
        "object": "list",
        "total_count": 0,
        "has_more": false,
        "url": "/v1/charges/ch_16l0eLHelsSEUOiEaPKtxBWj/refunds",
        "data": []
      }
    }
  }
}
```

<h2>Authentication</h2>
All endpoints are protected with Token Authentication. You must set up a token with a realm of 'stripe' for these endpoints to work properly.
