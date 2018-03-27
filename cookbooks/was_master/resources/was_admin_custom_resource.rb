# To learn more about Custom Resources, see https://docs.chef.io/custom_resources.html
#ruby_block "Call WAS Admin" do
#    block do
#      Chef::Resource::RubyBlock.send(:include, Chef::Mixin::ShellOut)
#      command1 = "command #{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption \"#{node['was']['java_option_first']}\" -javaoption \"#{node['was']['java_option_second']}\" -f #{node['was']['jython_path']}/#{jython_script_name}"
#      command_out = shell_out(command1)
#      node.run_state['output_from_run'] = command_out1.stdout
#    end
#    action :create
#  end
