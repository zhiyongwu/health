import db
import Levenshtein
import math

_CACHES = {

}


def _fill_cache():
    sql = "select `id`,name,`alias` from food_purine"
    cursor = db.cursor()
    cursor.execute(sql)
    for each in cursor:
        _id, name, alias = each
        name_arr = [name]
        if alias:
            alias_arr = alias.split(',')
            name_arr.extend(alias_arr)
        _CACHES[_id] = name_arr
    cursor.close()


def similarity(s1, s2):
    return 1 - Levenshtein.distance(s1, s2) / max(len(s1), len(s2))


def max_similarity(s1, arr):
    return max([similarity(s1, e) for e in arr])


def query_data(name):
    if not _CACHES:
        _fill_cache()
    candidates = []
    max_score = 0
    for _id in _CACHES.keys():
        name_arr = _CACHES[_id]
        max_simi = max_similarity(name, name_arr)
        if max_simi != 0:
            if max_simi > max_score:
                candidates = [_id]
                max_score = max_simi
            elif max_simi == max_score:
                candidates.append(_id)
    if not candidates:
        return None
    sql = "select * from food_purine where id in (%s)" % (','.join([str(e) for e in candidates]))
    cursor = db.cursor()
    cursor.execute(sql)
    result = []
    for each in cursor:
        _, name, value, alias = each
        result.append(
            {
                'name': name,
                'alias': alias,
                'value': value
            }
        )
    cursor.close()
    return result


if __name__ == '__main__':
    print(query_data("大头菜"))
