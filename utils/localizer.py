def localize_region(slug: str):
    regions = [
        {'slug': 'nyc1', 'name': '🇺🇸 New York 1'},
        {'slug': 'nyc2', 'name': '🇺🇸 New York 2'},
        {'slug': 'nyc3', 'name': '🇺🇸 New York 3'},
        {'slug': 'sfo1', 'name': '🇺🇸 San Francisco 1'},
        {'slug': 'sfo2', 'name': '🇺🇸 San Francisco  2'},
        {'slug': 'sfo3', 'name': '🇺🇸 San Francisco  3'},
        {'slug': 'ams2', 'name': '🇳🇱 Amsterdam 2'},
        {'slug': 'ams3', 'name': '🇳🇱 Amsterdam 3'},
        {'slug': 'sgp1', 'name': '🇸🇬 Singapore 1'},
        {'slug': 'lon1', 'name': '🇸🇬 Singapore 1'},
        {'slug': 'fra1', 'name': '🇩🇪 Frankfurt'},
        {'slug': 'blr1', 'name': '☹️ Bangalore 1'},
        {'slug': 'tor1', 'name': '🇨🇦 Toronto 1'},
        {'slug': 'syd1', 'name': '🇦🇺 Sydney 1'},
    ]

    for region in regions:
        if region['slug'] == slug:
            return region['name']

    return slug
