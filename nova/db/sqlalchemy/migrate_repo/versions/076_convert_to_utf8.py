# vim: tabstop=4 shiftwidth=4 softtabstop=4

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

from sqlalchemy import MetaData

meta = MetaData()


def upgrade(migrate_engine):
    meta.bind = migrate_engine

    # NOTE (ironcamel): The only table we are not converting to utf8 here is
    # dns_domains. This table has a primary key that is 512 characters wide.
    # When the mysql engine attempts to convert it to utf8, it complains about
    # not supporting key columns larger than 1000.

    if migrate_engine.name == "mysql":
        migrate_engine.execute(
            "ALTER TABLE agent_builds CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE aggregate_hosts CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE aggregate_metadata CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE aggregates CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE auth_tokens CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE block_device_mapping CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE bw_usage_cache CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE certificates CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE compute_nodes CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE console_pools CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE consoles CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE fixed_ips CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE floating_ips CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute("SET foreign_key_checks = 0;"
            "ALTER TABLE instances CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE instance_actions CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE instance_faults CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE instance_info_caches CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE instance_metadata CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE instance_type_extra_specs"
            " CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE instance_types CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE iscsi_targets CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE key_pairs CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE migrate_version CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE migrations CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE networks CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE projects CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE provider_fw_rules CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE quotas CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE s3_images CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE security_group_instance_association"
            " CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE security_group_rules CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE security_groups CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE services CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE sm_backend_config CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE sm_flavors CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE sm_volume CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE snapshots CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE snapshots CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE user_project_association"
            " CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE user_project_role_association"
            " CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE user_role_association CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE users CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE virtual_interfaces CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE virtual_storage_arrays CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE volume_metadata CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE volumes CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE volume_type_extra_specs"
            " CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE volume_types CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute(
            "ALTER TABLE zones CONVERT TO CHARACTER SET utf8")
        migrate_engine.execute("SET foreign_key_checks = 1")
        migrate_engine.execute(
            "ALTER DATABASE nova DEFAULT CHARACTER SET utf8")
