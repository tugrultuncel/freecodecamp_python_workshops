distance_mi= 1
is_raining= True
has_bike=True
has_car=False
has_ride_share_app=True

if distance_mi==False:
    print('False')
elif distance_mi <=1 and not is_raining:
    print('True')
elif distance_mi <=1 and is_raining:
    print('False')
elif 1 < distance_mi <=6 and (not has_bike):
    print('False')
elif 1 < distance_mi <=6 and (has_bike):
    print('True')
elif distance_mi>6 and has_ride_share_app:
    print('True')
elif distance_mi>6 and has_car:
    print('True')
elif distance_mi>6 and (not has_ride_share_app or not has_car):
    print('False')
