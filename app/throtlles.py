from rest_framework.throttling import AnonRateThrottle


class MatriculaAnoRateThrotlle(AnonRateThrottle):
    rate = '5/day'