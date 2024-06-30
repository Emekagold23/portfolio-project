def paginate(query, page, per_page=20):
    return query.paginate(page, per_page, False)