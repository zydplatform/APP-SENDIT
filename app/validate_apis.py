# def invalid_inputs(parcel_name, parcel_weight, parcel_description, parcel_price, pickup, destination, status):
#     errors_found = {}
#     if not isinstance('parcel_name', str):
#         errors_found['parcel_name'] = 'parcel name must be a string'
#     if not isinstance('parcel_weight', float):
#         errors_found['parcel_weight'] = 'parcel weight must be a float'
#     if not isinstance('parcel_description', str):
#         errors_found['parcel_description'] = 'parcel description must be a string'
#     if not isinstance('parcel_price', int):
#         errors_found['parcel_price'] = 'parcel price must be an integer'
#     if not isinstance('pickup', str):
#         errors_found['pickup'] = 'pickup location must be a string'
#     if not isinstance('destination', str):
#         errors_found['destination'] = 'destination location must be a string'
#     if not isinstance('status', str):
#         errors_found['status'] = 'status must be a string'
#     return errors_found


# """ checking for empty error fields."""
# def empty_field(parcel_name, parcel_weight, parcel_description, parcel_price, pickup, destination, status):
#     errors_found = {}
#     if not parcel_name:
#         errors_found['parcel_name'] = 'parcel name is required'
#     if not parcel_weight:
#         errors_found['parcel_weigt'] = 'parcel weight is required'
#     if parcel_weight < 0:
#         errors_found['parcel_weight'] = 'Invalid parcel weight '
#     if not parcel_description:
#         errors_found['parcel_description'] = 'parcel description is required'
#     if not parcel_price:
#         errors_found['parcel_price'] = 'parcel price is required'
#     elif not parcel_price > 0:
#         errors_found['parcel_price'] = 'parcel price must be an integer'
#     if not pickup:
#         errors_found['pickup'] = 'parcel pick up location not specified'
#     if not destination:
#         errors_found['destination'] = 'parcel destination not specified'
#     if not status:
#         errors_found['status'] = 'status is not specified'
#     return errors_found
