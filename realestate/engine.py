"""Real Estate Property CRM and Lease Management Engine for ERPNext."""

from datetime import datetime, date
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class PropertyUnit(BaseModel):
    unit_code: str  # e.g. TOWER-A-1204
    project_name: str
    unit_type: str  # 2BHK, 3BHK, Commercial Shop, Penthouse
    carpet_area_sqft: float
    base_price: float
    status: str = "Available"  # Available, Booked, Leased, Maintenance


class LeaseContract(BaseModel):
    lease_id: str
    unit_code: str
    tenant_name: str
    tenant_phone: str
    monthly_rent: float
    security_deposit: float
    lease_start: str
    lease_end: str
    status: str = "Active"  # Active, Terminated, Expired


class RealEstateEngine:
    """Manages unit availability, tenant lease billing, and payment milestones."""

    def __init__(self):
        self.units: Dict[str, PropertyUnit] = {}
        self.leases: Dict[str, LeaseContract] = {}

    def book_unit(self, unit_code: str, buyer_name: str, token_amount: float) -> Dict[str, Any]:
        if unit_code not in self.units:
            raise ValueError(f"Property Unit {unit_code} not found")
        unit = self.units[unit_code]
        if unit.status != "Available":
            raise ValueError(f"Unit {unit_code} is already {unit.status}")

        unit.status = "Booked"
        return {
            "unit_code": unit_code,
            "buyer_name": buyer_name,
            "token_amount": token_amount,
            "balance_payable": unit.base_price - token_amount,
            "status": "Booking Confirmed",
        }

    def create_lease(self, contract: LeaseContract) -> LeaseContract:
        if contract.unit_code not in self.units:
            raise ValueError(f"Unit {contract.unit_code} not found")

        unit = self.units[contract.unit_code]
        unit.status = "Leased"
        self.leases[contract.lease_id] = contract
        return contract

    def generate_monthly_rent_invoice(self, lease_id: str, month: str) -> Dict[str, Any]:
        if lease_id not in self.leases:
            raise ValueError("Lease not found")

        lease = self.leases[lease_id]
        maintenance_charge = 2500.0
        gst = maintenance_charge * 0.18
        total_due = lease.monthly_rent + maintenance_charge + gst

        return {
            "invoice_number": f"RENT-{lease_id}-{month}",
            "tenant": lease.tenant_name,
            "unit_code": lease.unit_code,
            "rent_amount": lease.monthly_rent,
            "maintenance_fee": maintenance_charge,
            "tax": gst,
            "total_due": total_due,
            "due_date": f"{month}-05",
        }
