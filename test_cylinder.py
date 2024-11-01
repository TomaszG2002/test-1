"""
TPRG 2131 Fall 2024 Test 1

Tomasz Giedrojc
100793058


"""

from cylinder import volume_cylinder, area_cylinder

def test_volume_cylinder():
    assert round(volume_cylinder(1, 2), 4) == 1.5708
    assert round(volume_cylinder(0.1, 4), 4) == 0.0314
    assert round(volume_cylinder(2, 1), 4) == 3.1416

def test_area_cylinder():
    assert round(area_cylinder(1, 2), 4) == 7.8540
    assert round(area_cylinder(0.1, 4), 4) == 1.2723
    assert round(area_cylinder(2, 1), 4) == 12.5664

def test_volume_cylinder_negative_height():
    with pytest.raises(ValueError, match="Make sure the height is postive."):
        volume_cylinder(1, -2)

def test_area_cylinder_negative_height():
    with pytest.raises(ValueError, match="make sure the height is postive."):
        area_cylinder(1, -2)
