# -*- coding: UTF-8 -*-
"""URL dispatcher for staffing module
@author: Sébastien Renard (sebastien.renard@digitalfox.org)
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

from django.urls import re_path
import staffing.views as v
import staffing.tables as t
import staffing.api as a

staffing_urls = [ re_path(r'^pdcreview/?$', v.pdc_review, name='pdcreview-index'),
                  re_path(r'^pdcreview/(?P<year>\d+)/(?P<month>\d+)/?$', v.pdc_review, name='pdcreview'),
                  re_path(r'^pdc_optim/$', v.optimise_pdc, name="optimise_pdc"),
                  re_path(r'^production-report/?$', v.prod_report, name='prod_report'),
                  re_path(r'^production-report/(?P<year>\d+)/(?P<month>\d+)/?$', v.prod_report, name='prod_report'),
                  re_path(r'^fixed-price-mission-report/?$', v.fixed_price_missions_report, name="fixed_price_missions_report"),
                  re_path(r'^mission/$', v.missions, name='missions'),
                  re_path(r'^mission/all', v.missions, {'onlyActive': False}, 'all-missions'),
                  re_path(r'^mission/(?P<mission_id>\d+)/$', v.mission_home, name="mission_home"),
                  re_path(r'^mission/update/$', v.mission_update, name="mission_inline_update"),
                  re_path(r'^mission/(?P<pk>\d+)/update$', v.MissionUpdate.as_view(), name='mission_update'),
                  re_path(r'^mission/newfromdeal/(?P<lead_id>\d+)/$', v.create_new_mission_from_lead, name="create_new_mission_from_lead"),
                  re_path(r'^forecast/mission/(?P<mission_id>\d+)/$', v.mission_staffing, name="mission_staffing"),
                  re_path(r'^mission/(?P<mission_id>\d+)/deactivate$', v.deactivate_mission, name="deactivate_mission"),
                  re_path(r'^forecast/consultant/(?P<consultant_id>\d+)/$', v.consultant_staffing, name="consultant_staffing"),
                  re_path(r'^forecast/mass/$', v.mass_staffing, name="mass_staffing"),
                  re_path(r'^timesheet/global/?$', v.all_timesheet, name="all_timesheet"),
                  re_path(r'^timesheet/global/(?P<year>\d+)/(?P<month>\d+)/?$', v.all_timesheet, name="all_timesheet"),
                  re_path(r'^timesheet/detailed/?$', v.detailed_csv_timesheet, name="detailed_csv_timesheet"),
                  re_path(r'^timesheet/detailed/(?P<year>\d+)/(?P<month>\d+)/?$', v.detailed_csv_timesheet, name="detailed_csv_timesheet"),
                  re_path(r'^timesheet/consultant/(?P<consultant_id>\d+)/$', v.consultant_timesheet, name="consultant_timesheet"),
                  re_path(r'^timesheet/consultant/(?P<consultant_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/?$', v.consultant_timesheet, name="consultant_timesheet"),
                  re_path(r'^timesheet/consultant/(?P<consultant_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<week>\d+)/?$', v.consultant_timesheet, name="consultant_timesheet"),
                  re_path(r'^timesheet/mission/(?P<mission_id>\d+)/$', v.mission_timesheet, name="mission_timesheet"),
                  re_path(r'^holidays_planning/?$', v.holidays_planning, name="holidays_planning"),
                  re_path(r'^holidays_planning/(?P<year>\d+)/(?P<month>\d+)/?$', v.holidays_planning, name="holidays_planning"),
                  re_path(r'^holidays_report/(?P<year>\d+)$', v.missions_report, {"nature": "HOLIDAYS"}, name="holidays-pivotable-year"),
                  re_path(r'^holidays_report/?$', v.missions_report, {"nature": "HOLIDAYS"}, name="holidays-pivotable"),
                  re_path(r'^holidays_report/all$', v.missions_report, {"nature": "HOLIDAYS", "year": "all"}, name="holidays-pivotable-all"),
                  re_path(r'^non-prod_report/(?P<year>\d+)$', v.missions_report, {"nature": "NONPROD"}, name="nonprod-pivotable-year"),
                  re_path(r'^non-prod_report/?$', v.missions_report, {"nature": "NONPROD"}, name="nonprod-pivotable"),
                  re_path(r'^non-prod_report/all$', v.missions_report, {"nature": "NONPROD", "year": "all"}, name="nonprod-pivotable-all"),
                  re_path(r'^contacts/mission/(?P<mission_id>\d+)/$', v.mission_contacts, name="mission_contacts"),
                  re_path(r'^rate/?$', v.mission_consultant_rate, name="mission_consultant_rate"),
                  re_path(r'^pdc-detail/(?P<consultant_id>\d+)/(?P<staffing_date>\d+)/?$', v.pdc_detail, name="pdc_detail"),
                  re_path(r'^datatable/all-missions/data/$', t.MissionsTableDT.as_view(), name='all_mission_table_DT'),
                  re_path(r'^datatable/active-missions/data/$', t.ActiveMissionsTableDT.as_view(), name='active_mission_table_DT'),
                  re_path(r'^datatable/clientcompany-missions/(?P<clientcompany_id>\d+)/data/$', t.ClientCompanyActiveMissionsTablesDT.as_view(), name='client_company_mission_table_DT'),
                  re_path(r'^turnover-pivotable/$', v.turnover_pivotable, name="turnover_pivotable"),
                  re_path(r'^turnover-pivotable/(?P<year>\d+)$', v.turnover_pivotable, name="turnover_pivotable_year"),
                  re_path(r'^turnover-pivotable/all$', v.turnover_pivotable, {"year": "all"}, name="turnover_pivotable_all"),
                  re_path(r'^lunch-tickets-pivotable$', v.lunch_tickets_pivotable, name="lunch_tickets_pivotable"),
                  re_path(r'^rate_objective_report/?$', v.rate_objective_report, name="rate_objective_report"),
                  re_path(r'^rates_report/?$', v.rates_report, name="rates_report"),
                  re_path(r'^graph/timesheet-rates/?$', v.graph_timesheet_rates_bar, name="graph_timesheet_rates_bar"),
                  re_path(r'^graph/timesheet-rates/team/(?P<team_id>\d+)$', v.graph_timesheet_rates_bar, name="graph_timesheet_rates_bar"),
                  re_path(r'^graph/profile-rates/?$', v.graph_profile_rates, name="graph_profile_rates"),
                  re_path(r'^graph/profile-rates/team/(?P<team_id>\d+)$', v.graph_profile_rates, name="graph_profile_rates"),
                  re_path(r'^graph/rates/consultant/(?P<consultant_id>\d+)', v.graph_consultant_rates, name="graph_consultant_rates"),
                  re_path(r'^api/mission_list/?$', a.mission_list, name="mission_list"),
                  re_path(r'^api/mission_list/(?P<start_date>\d{6})/?$', a.mission_list, name="mission_list"),
                  re_path(r'^api/mission_list/(?P<start_date>\d{6})/(?P<end_date>\d{6})/?$', a.mission_list, name="mission_list"),
                ]
