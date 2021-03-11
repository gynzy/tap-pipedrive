import singer
from tap_pipedrive.stream import PipedriveIterStream

class DealsParticipantsStream(PipedriveIterStream):
    base_endpoint = 'deals'
    id_endpoint = 'deals/{}/participants'
    schema = 'deal_participants'
    state_field = None
    key_properties = ['id']

    def get_name(self):
        return self.schema

    def update_endpoint(self, deal_id):
        self.endpoint = self.id_endpoint.format(deal_id)
