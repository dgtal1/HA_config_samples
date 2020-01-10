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

# validate
if validate(logger, target_state, entity_ids):
    ent_ids_switch = []
    ent_ids_light = []
    for entity_id in entity_ids:
        domain = entity_id.split('.')[0]
        if domain == 'switch':
            ent_ids_switch.append(entity_id)
        if domain == 'light':
            ent_ids_light.append(entity_id)            
    
    if ent_ids_switch:
        service_data = {"entity_id": entity_ids}
        hass.services.call("switch", "turn_"+target_state, service_data, False)

    if ent_ids_light:
        service_data = {"entity_id": entity_ids}
        hass.services.call("light", "turn_"+target_state, service_data, False)
