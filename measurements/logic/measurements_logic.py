from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_id):
    measurement = Measurement.objects.get(pk=(mea_id))
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.value = new_mea["value"]
    measurement.unit = new_mea["unit"]
    measurement.place = new_mea["place"]
    measurement.dateTime = new_mea["dateTime"]
    measurement.save()
    return measurement

def create_measurement(mea):
    measurement = Measurement(variable=mea["variable"],
                              value=mea["value"],
                              unit=mea["unit"],
                              place=mea["place"])
    measurement.save()
    return measurement