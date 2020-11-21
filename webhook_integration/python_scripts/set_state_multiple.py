""" 
SCRIPT INPUT - JSON MESSAGE:
{
    "entities": [
        {
            "input_boolean.switchable": {
                "state": "off"
            }
        },
        {
            "switch.kitchen": {
                "state": "on"
            }
        },
        {
            "light.entrance": {
                "state": "on"
            }
        },
        {
            "senor.temperature": {
                "state": "22.1"
            }
        },
        {
            "binary_senor.pir_entrance": {
                "state": "on"
            }
        }
    ]
}
Supported domains: as above
"""
def add_entity_state(state_dict, entity_id, state):         #(state_dict: dict, entity_id: str, state: str):
    
    list_on = state_dict.get('on')
    list_off = state_dict.get('off')
    list_state = state_dict.get('state')
    dict_state = {'entity_id': entity_id, 'state': state}

    if state == "on" and list_on is not None:
        list_on.append(entity_id)
    elif state == "off" and list_off is not None:
        list_off.append(entity_id)
    elif list_state is not None:
        list_state.append(dict_state)

entities = data.get('payload').get('entities')

domain_states = {                                   
    "switch": {"on": [], "off": []},                   # list element: entity_id
    "light": {"on": [], "off": []},                    # list element: entity_id
    "input_boolean": {"on": [], "off": []},            # list element: entity_id
    "sensor": {"state": []},                           # list element: {'entity_id': entity_id, 'state': state}
    "binary_sensor": {"state": []}                     # list element: {'entity_id': entity_id, 'state': state}
}

for entity in entities:   
    for entity_id, data in entity.items():

        domain = entity_id.split('.')[0]
        state = data.get('state')
        state_dict = {}

        if domain == 'switch':
            state_dict = domain_states.get(domain)
        if domain == 'light':
            state_dict = domain_states.get(domain)
        if domain == 'input_boolean':
            state_dict = domain_states.get(domain)
        if domain == 'sensor':
            state_dict = domain_states.get(domain)
        if domain == 'binary_sensor':
            state_dict = domain_states.get(domain)
        
        if state_dict:
            add_entity_state(state_dict, entity_id, state)


for domain, state_dict in domain_states.items():
    for state_kind, data_list in state_dict.items():
        if not data_list:
            continue
        if state_kind == 'state':
            for state_data in data_list:
                entity_id = state_data.get('entity_id')
                state     = state_data.get('state')
                state_obj = hass.states.get(entity_id)
                hass.states.set(entity_id, state, state_obj.attributes)
        else:
            service_data = {"entity_id": data_list}
            service = f"turn_{state_kind}"
            hass.services.call(domain, service, service_data, False)
