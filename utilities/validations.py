from api.location.models import CountryType, TimeZoneType

# new file was created as imports are not possible in utility file


def validate_country_field(**kwargs):
    """
    Function to validate country fields when
    saving an object
    :params kwargs
    """
    valid_countries = [country.value for country in CountryType]
    country_name = kwargs['country']
    if country_name not in valid_countries:
        raise AttributeError("Not a valid country")


def validate_timezone_field(**kwargs):
    """
    Function to validate country fields when
    saving an object
    :params kwargs
    """
    timezones = [timezone.name for timezone in TimeZoneType]
    time_zone = kwargs['time_zone']
    if time_zone not in timezones:
        raise AttributeError("Not a valid time zone")
