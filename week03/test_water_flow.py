from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

def test_water_column_height():
    assert water_column_height(0,0) == 0
    assert water_column_height(0,10) == 7.5
    assert water_column_height(25,0) == 25
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001) #0.001
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75)==approx(0, abs=0.001)	#0.001
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0)==approx(0, abs=0.001)	#0.001
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75)==approx(-113.008, abs=0.001)	#0.001
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65)==approx(-100.462, abs=0.001)	#0.001
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65)==approx(-61.576, abs=0.01)	#0.001
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65)==approx(-110.884, abs=0.001)	#0.001

def test_pressure_loss_from_fittings():
#V	Q  P approx

# 0	    3	0	0.001
# 1.65	0	0	0.001
# 1.65	2	-0.109	0.001
# 1.75	2	-0.122	0.001
# 1.75	5	-0.306	0.001

    assert pressure_loss_from_fittings(0, 3)==approx(0, abs=0.001)    
    assert pressure_loss_from_fittings(1.65, 0)==approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2)==approx(-0.109,abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2)==approx(-0.122,abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5)==approx(-0.306,abs=0.001)
    # assert pressure_loss_from_fittings()==approx(,abs=0.001)

def test_reynolds_number():
#0.048692	0	    0  	    1
#0.048692	1.65	80069	1
#0.048692	1.75	84922	1
#0.28687	    1.65	471729	1
#0.28687	    1.75	500318	1
    assert reynolds_number(0.048692,0)==approx(0,abs=1)
    assert reynolds_number(0.048692,1.65)==approx(80069,abs=1)
    assert reynolds_number(0.048692,1.75)==approx(84922,abs=1)
    assert reynolds_number(0.28687,1.65)==approx(471729,abs=1)
    assert reynolds_number(0.28687,1.75)==approx(500318,abs=1)

def test_pressure_loss_from_pipe_reduction():
# 0.28687	0	1	0.048692	0	0.001
# 0.28687	1.65	471729	0.048692	-163.744	0.001
# 0.28687	1.75	500318	0.048692	-184.182	0.001
    assert pressure_loss_from_pipe_reduction(0.28687,0,1,0.048692)==approx(0,abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.65,471729,0.048692)==approx(-163.744,abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.75,500318,0.048692)==approx(-184.182,abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])