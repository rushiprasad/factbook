import json
import pkg_resources
import requests

BASE_URL = 'https://www.cia.gov/library/publications/the-world-factbook/geos/'
resource_package = __name__


class UnknownCountryIdentifier(KeyError):
    pass


def _convert_country_identifier(country_identifier: str) -> str:
    """Converts the country identifier to a country abbreviation.

    Args:
        country_identifier: the country abbreviation or country name.

    Returns:
        String - the country abbreviation associated with the given identifier.

    """
    country_code_map = json.loads(
        pkg_resources.resource_stream(
            resource_package,
            'data/country_codes.json'
        ).read().decode('utf-8')
    )
    country_abbrev = country_code_map.get(country_identifier)
    if country_abbrev:
        return country_abbrev
    elif country_identifier in country_code_map.values():
        return country_identifier
    else:
        raise UnknownCountryIdentifier('unable to find country_identifier: ' +
                                       country_identifier)


def extract(country_identifier: str) -> dict:
    """Extracts data for an individual country abbrev or name from the CIA site.

    Args:
        country_identifier: the country abbrev or country name.

    Returns:
        Dictionary containing the CIA World Factbook data for the country.

    """
    country_code = _convert_country_identifier(country_identifier)
    resp = requests.get(BASE_URL + 'print_' + country_code + '.html')
    print(resp.content)
    return {}


def extract_all(use_existing_codes: bool = False) -> dict:
    """Extracts data for all known country codes.

    Args:
        use_existing_codes: If `False`, use the latest country abbrev mappings
            from the site. If `True`, use the existing codes that are already
            present in the repository. Default is `False`.

    Returns:
        Dictionary containing the CIA World Factbook data for all countries.

    """
    return {}


def get(country_identifier: str) -> dict:
    """Retrieves the country data associated with a country code or name from
       the country file located in the repository.

    Args:
        country_identifier: the country code or country name.

    Returns:
        Dictionary containing the CIA World Factbook data for the country.

    """
    return {}
