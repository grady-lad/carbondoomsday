"""View filters."""

import rest_framework_filters as filters

from carbondoomsday.carbondioxide.models import CO2Measurement


class CO2MeasurementFilter(filters.FilterSet):
    """CO2 measurement view filters."""
    class Meta:
        model = CO2Measurement
        fields = {
            "ppm": "__all__",
            "date": "__all__",
        }
