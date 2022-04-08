from geopy import Nominatim
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types.message import ContentTypes
from states.states import Registration
from loader import dp


@dp.message_handler(content_types=ContentTypes.LOCATION,state=Registration.manzil)
async def location(message: types.Message, state: FSMContext):
    location =  message.location
    latitude = f"{location['latitude']}"
    longitude = f"{location['longitude']}"
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        locat = geolocator.reverse(latitude+","+longitude)
        address = locat.raw['address']
        a = ['house_number','display_name','road','postcode','residential','county','city']
        manzil = []
        for i in a:
            try:
                k = address[f'{i}']
                manzil.append(k)
            except:
                pass
        print(manzil)
    except:
        pass