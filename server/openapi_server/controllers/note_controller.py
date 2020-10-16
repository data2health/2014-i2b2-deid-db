import connexion
import os
import json
from flask import jsonify, make_response
from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util
from openapi_server.models.page_response import PageResponse
import openapi_server.db_connection as db
import logging


def notes_read(id_):  # noqa: E501
    """Get a clinical note by ID

    Returns the clinical note for a given ID # noqa: E501

    :param id: The ID of the clinical note to fetch
    :type id: str

    :rtype: Note
    """
    values = db.load_config()

    conn = db.get_connection_local_pg(values)
    cur = conn.cursor()
    select_notes = 'SELECT id, filename, text from i2b2_data.public.pat_notes where id = %s'
    cur.execute(select_notes, (id_,))
    all_rows = cur.fetchall()
    res = []
    for row in all_rows:
        id = row[0]
        dict = {'id': id, 'fileName': row[1], 'text': row[2]}
        res.append(dict)

    return jsonify(items=res)


def notes_read_all(limit=None):  # noqa: E501
    """Get all clinical notes , if limit not included in request it assumes the min count which is 10

    Returns the clinical notes # noqa: E501

    :rtype: List[Note]
    """

    counter = 0
    res = []
    logging.info(f"notes_read_all  ")
    #if connexion.request.is_json:
    # limit =  AnyType.from_dict(connexion.request.get_json())
    values = db.load_config()

    conn = db.get_connection_local_pg(values)
    cur = conn.cursor()
    select_notes = 'SELECT id, filename, text from  i2b2_data.public.pat_notes'
    logging.info(f"query of {select_notes} with a limit of {limit}")
    cur.execute(select_notes)
    all_rows = cur.fetchall()
    counter= len(all_rows)

    for row in all_rows:
        id = row[0]
        dict = { 'id': id , 'fileName' : row[1], 'text':row[2] }
        res.append( dict )

    next = {"next" : "/api/v1/ui/#/Note/notes_read_all?limit=10" }
    data = {'links': next, 'items': res}
    # return jsonify(  data)
    return make_response(json.dumps(data, indent=4) )


def notes_update(id, note):  # noqa: E501
    """Update a clinical note by ID

    This can only be done by the logged in user. # noqa: E501

    :param id: Updates the clinical note for a given ID
    :type id: str
    :param note: Updated clinical note
    :type note: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        note = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
