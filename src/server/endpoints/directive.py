from fastapi import APIRouter
from endpoints.models import (DirectiveFrom, DirectiveTo, DirectiveFromUpdater, DirectiveToUpdater,
                              DirectiveId, DirectiveFromTo)
from resolvers.directive import (get_directive, post_directive, get_directive_to, get_directive_from,
                                 put_directive_from, put_directive_to, delete_directive, get_directive_all)
router = APIRouter()


@router.post('/new_directive')
def get_user_endpoint(endpoint: DirectiveFromTo):
    return post_directive(endpoint)


@router.get('/directive_all')
def get_user_endpoint():
    return get_directive_all()


@router.get('/directive')
def get_user_endpoint(endpoint: DirectiveFromTo):
    return get_directive(endpoint)


@router.get('/directive_from')
def get_user_endpoint(endpoint: DirectiveFrom):
    return get_directive_from(endpoint)


@router.get('/directive_to')
def get_user_endpoint(endpoint: DirectiveTo):
    return get_directive_to(endpoint)


@router.put('/directive_from')
def get_user_endpoint(endpoint: DirectiveFromUpdater):
    return put_directive_from(endpoint)


@router.put('/directive_to')
def get_user_endpoint(endpoint: DirectiveToUpdater):
    return put_directive_to(endpoint)


@router.delete('/directive')
def get_user_endpoint(endpoint: DirectiveId):
    return delete_directive(endpoint)
