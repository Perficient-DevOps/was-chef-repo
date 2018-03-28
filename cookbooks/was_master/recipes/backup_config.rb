#
# Cookbook:: was_master
# Recipe:: backup_config
#
# Copyright:: 2018, The Authors, All Rights Reserved.

execute "Run Backup" do
  command "#{node['was']['install_home']}bin/backupConfig.sh #{node['was']['backup_path']}.zip -nostop -logfile #{node['was']['backup_path']}.log -replacelog -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -profileName #{node['was']['profile_name']}"
  live_stream true
end
