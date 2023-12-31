import kivy
from dotenv import get_key
from kivy.core.window import Window
from kivymd.app import MDApp

from jira_connection_settings_popup import JiraConnectionSettingsPopup
from jira_issue_tracker import JiraIssueTracker

kivy.require('2.1.0')


class JiraTrackerApp(MDApp):

    def build(self):
        # Set the window size (overall size of the program)
        Window.size = (420, 335)  # Set your desired window size
        # Set the theme colors
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '200'
        # You can switch the 'Light' to 'Dark' based on user preference or a setting
        self.theme_cls.theme_style = 'Dark'

        # if there are not environment variables set in a .env file, then we need the user to put them in
        if not (get_key('.env', 'JIRA_API_TOKEN') and get_key('.env', 'JIRA_SITE_URL')):
            return JiraConnectionSettingsPopup()
        else:
            # the variables were set so we can attempt to use them to get information from Jira Server
            return JiraIssueTracker()


if __name__ == '__main__':
    JiraTrackerApp().run()
