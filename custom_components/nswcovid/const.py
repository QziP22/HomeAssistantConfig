"""Constants used by NSW Covid components."""
from __future__ import annotations

from typing import Final

DOMAIN: Final = "nswcovid"

INTEGRATION_VERSION: Final = "v0.0.25"

NSWHEALTH_HOST: Final = "www.health.nsw.gov.au"
NSWHEALTH_PATH: Final = "Infectious/covid-19/Pages/stats-nsw.aspx"

NSWHEALTH_NAME: Final = "Covid NSW"

NSWHEALTH_UPDATE: Final = f"{DOMAIN}_tracker_update"

ATTR_PUBLISHED: Final = "published"
ATTR_LOCALLY_ACTIVE: Final = "locally_active"
ATTR_INTERSTATE_ACTIVE: Final = "interstate_active"
ATTR_OVERSEAS_ACTIVE: Final = "overseas_active"
ATTR_TOTAL_ACTIVE: Final = "total_active"
ATTR_LAST_24_HOURS_KNOWN: Final = "last_24_hours_known"
ATTR_LAST_24_HOURS_UNKNOWN: Final = "last_24_hours_unknown"
ATTR_LAST_24_HOURS_INTERSTATE: Final = "last_24_hours_interstate"
ATTR_LAST_24_HOURS_OVERSEAS: Final = "last_24_hours_overseas"
ATTR_LAST_24_HOURS_TOTAL: Final = "last_24_hours_total"
ATTR_LAST_24_HOURS_TESTS: Final = "last_24_hours_tests"
ATTR_THIS_WEEK_KNOWN: Final = "this_week_known"
ATTR_THIS_WEEK_UNKNOWN: Final = "this_week_unknown"
ATTR_THIS_WEEK_INTERSTATE: Final = "this_week_interstate"
ATTR_THIS_WEEK_OVERSEAS: Final = "this_week_overseas"
ATTR_THIS_WEEK_TOTAL: Final = "this_week_total"
ATTR_THIS_WEEK_TESTS: Final = "this_week_tests"
ATTR_LAST_WEEK_KNOWN: Final = "last_week_known"
ATTR_LAST_WEEK_UNKNOWN: Final = "last_week_unknown"
ATTR_LAST_WEEK_INTERSTATE: Final = "last_week_interstate"
ATTR_LAST_WEEK_OVERSEAS: Final = "last_week_overseas"
ATTR_LAST_WEEK_TOTAL: Final = "last_week_total"
ATTR_LAST_WEEK_TESTS: Final = "last_week_tests"
ATTR_THIS_YEAR_KNOWN: Final = "this_year_known"
ATTR_THIS_YEAR_UNKNOWN: Final = "this_year_unknown"
ATTR_THIS_YEAR_INTERSTATE: Final = "this_year_interstate"
ATTR_THIS_YEAR_OVERSEAS: Final = "this_year_overseas"
ATTR_THIS_YEAR_TOTAL: Final = "this_year_total"
ATTR_THIS_YEAR_TESTS: Final = "this_year_tests"
ATTR_LAST_24_HOURS_FIRST_DOSE: Final = "last_24_hours_first_dose"
ATTR_LAST_24_HOURS_SECOND_DOSE: Final = "last_24_hours_second_dose"
ATTR_LAST_24_HOURS_TOTAL_DOSE: Final = "last_24_hours_total_dose"
ATTR_TOTAL_FIRST_DOSE: Final = "total_first_dose"
ATTR_TOTAL_SECOND_DOSE: Final = "total_second_dose"
ATTR_TOTAL_TOTAL_DOSE: Final = "total_total_dose"
ATTR_LIVES_LOST: Final = "lives_lost"
ATTR_LIVES_LOST_FEMALE_0_9: Final = "lives_lost_female_0_9"
ATTR_LIVES_LOST_FEMALE_10_19: Final = "lives_lost_female_10_19"
ATTR_LIVES_LOST_FEMALE_20_29: Final = "lives_lost_female_20_29"
ATTR_LIVES_LOST_FEMALE_30_39: Final = "lives_lost_female_30_39"
ATTR_LIVES_LOST_FEMALE_40_49: Final = "lives_lost_female_40_59"
ATTR_LIVES_LOST_FEMALE_50_59: Final = "lives_lost_female_50_59"
ATTR_LIVES_LOST_FEMALE_60_69: Final = "lives_lost_female_60_69"
ATTR_LIVES_LOST_FEMALE_70_79: Final = "lives_lost_female_70_79"
ATTR_LIVES_LOST_FEMALE_80_89: Final = "lives_lost_female_80_89"
ATTR_LIVES_LOST_FEMALE_90_PLUS: Final = "lives_lost_female_90_plus"
ATTR_LIVES_LOST_MALE_0_9: Final = "lives_lost_male_0_9"
ATTR_LIVES_LOST_MALE_10_19: Final = "lives_lost_male_10_19"
ATTR_LIVES_LOST_MALE_20_29: Final = "lives_lost_male_20_29"
ATTR_LIVES_LOST_MALE_30_39: Final = "lives_lost_male_30_39"
ATTR_LIVES_LOST_MALE_40_49: Final = "lives_lost_male_40_59"
ATTR_LIVES_LOST_MALE_50_59: Final = "lives_lost_male_50_59"
ATTR_LIVES_LOST_MALE_60_69: Final = "lives_lost_male_60_69"
ATTR_LIVES_LOST_MALE_70_79: Final = "lives_lost_male_70_79"
ATTR_LIVES_LOST_MALE_80_89: Final = "lives_lost_male_80_89"
ATTR_LIVES_LOST_MALE_90_PLUS: Final = "lives_lost_male_90_plus"
ATTR_CASES: Final = "cases"
ATTR_CASES_FEMALE_0_9: Final = "cases_female_0_9"
ATTR_CASES_FEMALE_10_19: Final = "cases_female_10_19"
ATTR_CASES_FEMALE_20_29: Final = "cases_female_20_29"
ATTR_CASES_FEMALE_30_39: Final = "cases_female_30_39"
ATTR_CASES_FEMALE_40_49: Final = "cases_female_40_59"
ATTR_CASES_FEMALE_50_59: Final = "cases_female_50_59"
ATTR_CASES_FEMALE_60_69: Final = "cases_female_60_69"
ATTR_CASES_FEMALE_70_79: Final = "cases_female_70_79"
ATTR_CASES_FEMALE_80_89: Final = "cases_female_80_89"
ATTR_CASES_FEMALE_90_PLUS: Final = "cases_female_90_plus"
ATTR_CASES_MALE_0_9: Final = "cases_male_0_9"
ATTR_CASES_MALE_10_19: Final = "cases_male_10_19"
ATTR_CASES_MALE_20_29: Final = "cases_male_20_29"
ATTR_CASES_MALE_30_39: Final = "cases_male_30_39"
ATTR_CASES_MALE_40_49: Final = "cases_male_40_59"
ATTR_CASES_MALE_50_59: Final = "cases_male_50_59"
ATTR_CASES_MALE_60_69: Final = "cases_male_60_69"
ATTR_CASES_MALE_70_79: Final = "cases_male_70_79"
ATTR_CASES_MALE_80_89: Final = "cases_male_80_89"
ATTR_CASES_MALE_90_PLUS: Final = "cases_male_90_plus"
ATTR_DOSES: Final = "doses"
ATTR_NSW_HEALTH_DOSES_DAILY: Final = "nsw_health_doses_daily"
ATTR_NSW_HEALTH_DOSES_CUMULATIVE: Final = "nsw_health_doses_cumulative"
ATTR_GP_NETWORK_DOSES_CUMULATIVE: Final = "gp_network_doses_cumulative"
ATTR_NSW_HEALTH_DOSES_UPDATED: Final = "nsw_health_doses_updated"
ATTR_GP_NETWORK_DOSES_UPDATED: Final = "gp_network_doses_updated"
ATTR_ALL_PROVIDERS_DOSES_CUMULATIVE: Final = "all_providers_doses_cumulative"

DEVICE_CLASS_COVID_CASES: Final = "covid_cases"
DEVICE_CLASS_COVID_VACCINATIONS: Final = "covid_vaccinations"

MANUFACTURER: Final = "NSW Health"
