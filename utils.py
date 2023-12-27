from ippanel import Client


def send_otp_code(phone_number, code, full_name):
    api_key = "rDQJQVV_wI1tP5QPc1BN4u8vYdcaTQM2GuSfKUeoqpw="
    message = f'{full_name} عزیز کد احراز شما: {code}'
    # create client instance
    sms = Client(api_key)
    message_id = sms.send(
        sender="+983000505",  # originator
        recipients=[phone_number, ],  # recipients
        message=message,  # message
        summary="description"  # is logged
    )
