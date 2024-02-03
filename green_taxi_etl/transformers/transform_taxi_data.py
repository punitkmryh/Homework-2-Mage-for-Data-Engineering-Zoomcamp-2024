if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
       # Remove rows where passenger count or trip distance is zero
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case
    data.columns = [col.lower() for col in data.columns]
    return data


@test
def test_output(output, *args) -> None:
    # Add assertions
    assert output['vendorid'].isin(output['vendorid']).all(), "Assertion Error: vendor_id should be one of the existing values in the column"
    assert (output['passenger_count'] > 0).all(), "Assertion Error: passenger_count should be greater than 0"
    assert (output['trip_distance'] > 0).all(), "Assertion Error: trip_distance should be greater than 0"
