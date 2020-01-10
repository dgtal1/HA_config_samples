def validate(logger, state, entity_id):
    if not entity_id:
        logger.error('No entity_id provided')
        return False
    if not state:
        logger.error('No state provided')
        return False
    
    return True

target_state = data.get('state')
entity_ids = data.get('entity_ids')

# validate parameters
if validate(logger, target_state, entity_ids):
    service_data = {"entity_id": entity_ids}
    hass.services.call("switch", "turn_"+target_state, service_data, False)
