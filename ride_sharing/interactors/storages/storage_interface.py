import abc
from ride_sharing.interactors.storages.dtos.dtos import RideRequestDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_ride_request(self, ride_request: RideRequestDTO):
        pass
