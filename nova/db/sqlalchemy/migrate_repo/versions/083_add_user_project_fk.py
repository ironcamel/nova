# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sqlalchemy import MetaData, Table
from migrate import ForeignKeyConstraint

from nova import log as logging

LOG = logging.getLogger(__name__)


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    user_project = Table('user_project_association', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    projects = Table('projects', meta, autoload=True)

    try:
        ForeignKeyConstraint(columns=[user_project.c.project_id],
                             refcolumns=[projects.c.id]).create()
        ForeignKeyConstraint(columns=[user_project.c.user_id],
                             refcolumns=[users.c.id]).create()
    except Exception:
        LOG.error(_("Foreign key constraints couldn't be added"))
        raise


def downgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    user_project = Table('user_project_association', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    projects = Table('projects', meta, autoload=True)

    try:
        ForeignKeyConstraint(columns=[user_project.c.project_id],
                             refcolumns=[projects.c.id]).drop()
        ForeignKeyConstraint(columns=[user_project.c.user_id],
                             refcolumns=[users.c.id]).drop()
    except Exception:
        LOG.error(_("Foreign key constraints couldn't be dropped"))
        raise
