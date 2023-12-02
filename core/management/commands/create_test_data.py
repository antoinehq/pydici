# coding: utf-8

"""
Create test / demo data

@author: Sébastien Renard (sebastien.renard@digitalfox.org)
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""
import random
from datetime import date, datetime, timedelta

from django.core.management import BaseCommand
from django.db.models import F
from django.contrib.auth.models import User, Group

from crm.factories import SubsidiaryFactory, CompanyFactory, SupplierFactory
from crm.models import BusinessSector, Subsidiary
from people.factories import CONSULTANT_PROFILES, ConsultantFactory, UserFactory, DailyRateObjectiveFactory, ProductionRateObjectiveFactory
from people.models import ConsultantProfile, Consultant
from core.models import GroupFeature, FEATURES
from leads.factories import LeadFactory
from leads.models import Lead

N_SUBSIDIARIES = 3
N_CONSULTANTS = 50
N_COMPANIES = 30
N_SUPPLIERS = 5
N_LEADS = 200

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        create_static_data()

        # Subsidiary
        SubsidiaryFactory.create_batch(N_SUBSIDIARIES)

        # Peoples
        ConsultantFactory.create_batch(N_CONSULTANTS)
        UserFactory.create_batch(N_CONSULTANTS)
        DailyRateObjectiveFactory.create_batch(N_CONSULTANTS)
        ProductionRateObjectiveFactory.create_batch(N_CONSULTANTS)
        set_managers()
        set_user_permissions()

        # Client and suppliers
        CompanyFactory.create_batch(N_COMPANIES)
        SupplierFactory.create_batch(N_SUPPLIERS)

        # Leads
        LeadFactory.create_batch(N_LEADS)
        set_lead_state()
        lastweek = datetime.now() - timedelta(days=7)
        Lead.objects.all().update(update_date=lastweek)


def create_static_data():
    # Business sector
    for bs in ["Information Technology", "Health Care", "Financials", "Consumer Goods",
               "Communication Services", "Industrials", "Energy", "Utilities", "Real Estate", "Materials"]:
        BusinessSector(name=bs).save()

    # Consultant profiles
    for level, profile in enumerate(CONSULTANT_PROFILES):
        ConsultantProfile(name=profile, level=level).save()
    ConsultantProfile(name="support", level=3).save()

def set_managers():
    Consultant.objects.filter(profil__name="director").update(manager=F("id"), staffing_manager=F("id"))
    for subsidiary in Subsidiary.objects.all():
        managers = Consultant.objects.filter(company=subsidiary, profil__name__in=("manager", "director"))
        for consultant in Consultant.objects.filter(company=subsidiary):
            manager = random.choice(managers)
            consultant.manager = manager
            consultant.staffing_manager = manager
            consultant.save()

def set_user_permissions():
    consultants_group = Group(name="consultants")
    consultants_group.save()
    for feature in FEATURES:
        GroupFeature(group=consultants_group, feature=feature).save()
    consultants_group.user_set.add(*User.objects.all())
    u = User.objects.first()
    u.is_superuser = True
    u.is_staff = True
    u.save()

def set_lead_state():
    for lead in Lead.objects.filter(creation_date__gt=(date.today()-timedelta(90))):
        lead.state = random.choice([s[0] for s in Lead.STATES])
        lead.save()
    for lead in Lead.objects.filter(creation_date__lte=(date.today()-timedelta(90))):
        lead.state = random.choice([s[0] for s in Lead.STATES[4:]])
        lead.save()
