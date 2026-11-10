"""Unit tests for RealEstateEngine."""

from realestate.engine import RealEstateEngine, PropertyUnit, LeaseContract


def test_property_booking_and_lease():
    engine = RealEstateEngine()
    unit = PropertyUnit(
        unit_code="TOWER-B-501",
        project_name="Greenwood Heights",
        unit_type="2BHK",
        carpet_area_sqft=850.0,
        base_price=6500000.0,
    )
    engine.units[unit.unit_code] = unit

    # Book unit
    booking = engine.book_unit(unit.unit_code, buyer_name="Anita Sharma", token_amount=500000.0)
    assert booking["status"] == "Booking Confirmed"
    assert engine.units[unit.unit_code].status == "Booked"

    # Test lease invoice
    lease = LeaseContract(
        lease_id="LS-102",
        unit_code=unit.unit_code,
        tenant_name="Karan Malhotra",
        tenant_phone="9820011223",
        monthly_rent=35000.0,
        security_deposit=100000.0,
        lease_start="2026-01-01",
        lease_end="2026-12-31",
    )
    engine.create_lease(lease)
    inv = engine.generate_monthly_rent_invoice("LS-102", "2026-11")
    assert inv["rent_amount"] == 35000.0
    assert inv["total_due"] > 35000.0
