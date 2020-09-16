# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.testbootstrap -t test_portlet.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.testbootstrap.testing.NVA_TESTBOOTSTRAP_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/testbootstrap/tests/robot/test_portlet.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Portlet
  Given a logged-in site administrator
    and an add Portlet form
   When I type 'My Portlet' into the title field
    and I submit the form
   Then a Portlet with the title 'My Portlet' has been created

Scenario: As a site administrator I can view a Portlet
  Given a logged-in site administrator
    and a Portlet 'My Portlet'
   When I go to the Portlet view
   Then I can see the Portlet title 'My Portlet'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Portlet form
  Go To  ${PLONE_URL}/++add++Portlet

a Portlet 'My Portlet'
  Create content  type=Portlet  id=my-portlet  title=My Portlet

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Portlet view
  Go To  ${PLONE_URL}/my-portlet
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Portlet with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Portlet title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
