# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s hmn.university -t test_course_content.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src hmn.university.testing.HMN_UNIVERSITY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/hmn/university/tests/robot/test_course_content.robot
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

Scenario: As a site administrator I can add a Course content
  Given a logged-in site administrator
    and an add Course form
   When I type 'My Course content' into the title field
    and I submit the form
   Then a Course content with the title 'My Course content' has been created

Scenario: As a site administrator I can view a Course content
  Given a logged-in site administrator
    and a Course content 'My Course content'
   When I go to the Course content view
   Then I can see the Course content title 'My Course content'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Course form
  Go To  ${PLONE_URL}/++add++Course

a Course content 'My Course content'
  Create content  type=Course  id=my-course_content  title=My Course content

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Course content view
  Go To  ${PLONE_URL}/my-course_content
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Course content with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Course content title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
