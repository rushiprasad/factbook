from bs4 import BeautifulSoup
import json
import pkg_resources
import re
import requests
from typing import Dict

BASE_URL = 'https://www.cia.gov/library/publications/the-world-factbook/'
resource_package = __name__


class UnknownCountryIdentifier(KeyError):
    pass


def _extract_country_abbrev_map() -> Dict[str, str]:
    """Extracts the list of country names : country abbreviations from the site.

    Returns:
        Dict[str, str] - key : value, country name : country abbreviation

    """
    resp = requests.get(BASE_URL + 'print/textversion.html')
    soup = BeautifulSoup(resp.content, "html.parser")
    abbrev_link_regex = '^[.]{2}[/]geos[/]([a-z]{2})[.]html$'
    country_links = soup.select('select.selecter_links > option')
    country_abbrev_map = {}
    for link in country_links:
        regex_match = re.match(abbrev_link_regex, link['value'])
        if regex_match:
            country_abbrev_map[link.get_text().strip()] = regex_match.group(1)
    return country_abbrev_map


def _convert_country_identifier(country_identifier: str) -> str:
    """Converts the country identifier to a country abbreviation.

    Args:
        country_identifier: the country abbreviation or country name.

    Returns:
        String - the country abbreviation associated with the given identifier.

    """

    country_abbrev_map = json.loads(
        pkg_resources.resource_stream(
            resource_package,
            'data/country_abbrev_map.json'
        ).read().decode()
    )
    country_abbrev = country_abbrev_map.get(country_identifier)
    if country_abbrev:
        return country_abbrev
    elif country_identifier in country_abbrev_map.values():
        return country_identifier
    else:
        raise UnknownCountryIdentifier('unable to find country_identifier: ' +
                                       country_identifier)


def _parse_country_html_(html: str) -> dict:
    """Parses country html to a sanitized dict containing the factbook data

    Args:
        html: the html string of the country's factbook page

    Returns:
        Dictionary containing the CIA World Factbook data for the country.

    """
    return {}


def extract(country_identifier: str) -> dict:
    """Extracts data for an individual country abbrev or name from the CIA site.

    Args:
        country_identifier: the country abbrev or country name.

    Returns:
        Dictionary containing the CIA World Factbook data for the country.

    """
    country_code = _convert_country_identifier(country_identifier)
    resp = requests.get(BASE_URL + 'geos/print_' + country_code + '.html')
    return _parse_country_html_(resp.text)


def extract_all(use_existing_codes: bool = False) -> dict:
    """Extracts data for all known country abbreviations.

    Args:
        use_existing_codes: If `False`, use the latest country abbrev mappings
            from the site. If `True`, use the existing codes that are already
            present in the repository. Default is `False`.

    Returns:
        Dictionary containing the CIA World Factbook data for all countries.

    """
    return {}


def get(country_identifier: str) -> dict:
    """Retrieves the country data associated with a country abbrev or name from
       the country file located in the repository.

    Args:
        country_identifier: the country abbrev or country name.

    Returns:
        Dictionary containing the CIA World Factbook data for the country.

    """
    return {}
