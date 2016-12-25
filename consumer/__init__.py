""" Consumer package

Contains models and functions to consume font repository API and cache details.
Goal is to update FMS cache data and generate repository cdn links for fonts to
associate Electron UI.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

from consumer.GitHubConsumer import GitHubConsumer
from consumer.GitLabConsumer import GitLabConsumer
from consumer.FontmanConsumer import FontmanConsumer
