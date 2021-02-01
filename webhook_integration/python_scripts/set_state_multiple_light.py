""" 
SCRIPT INPUT - JSON MESSAGE:
{
    "entities": [
         {
            "sensor__xiaomi_clock_salon_temperature":  "24.1"
        },
         {
            "switch__room":  "on"
        }        
    ]
}
"""

entities = data.get('payload').get('entities')

for entity in entities:   
    for entity_id, state in entity.items():

        split = entity_id.split('__')
        domain = split[0]
        name = split[1]
        entity = f"{domain}.{name}"

        state_obj = hass.states.get(entity)
        hass.states.set(entity, state, state_obj.attributes)
