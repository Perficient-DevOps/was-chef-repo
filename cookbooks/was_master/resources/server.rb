# To learn more about Custom Resources, see https://docs.chef.io/custom_resources.html

resource_name :server

property :name, String, default: 'default'

action :create do

end

action :delete do
  
end

action :start do

  jython_script = "#{ Chef::Config[:file_cache_path] }/script.py"

  file jython_script do
    content "AdminServerManagement.startSingleServer(#{node[:was][:node_name]},#{node[:was][:server_name]},'YES')"
    owner node[:was][:run_user]
    group node[:was][:run_group]
    mode '0755'
    action :create
  end

  execute "Run Jython" do
    command "#{node[:was][:install_home]}bin/wsadmin.sh -conntype SOAP -host #{ node[:was][:host] } -port #{ node[:was][:soap_port] } -lang jython -user #{node[:was][:was_user]} -password #{node[:was][:was_pass]} -f #{jython_script}"
  end


end

action :stop do

end
