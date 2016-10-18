def extract(country_identifier: str) -> dict:
    """Extracts data for an individual country code or name from the CIA site.

    Args:
        country_identifier: the country code or country name.

    Returns:
        Dictionary containing the CIA World Factbook data for the country.

    """
    return {}


def extract_all(use_existing_codes: bool = False) -> dict:
    """Extracts data for all known country codes.

    Args:
        use_existing_codes: If `False`, use the latest country to country code
            mappings from the site. If `True`, use the existing codes that are
            already present in the repository. Default is `False`.

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
