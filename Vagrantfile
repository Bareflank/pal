Vagrant.configure(2) do |config|
    config.vm.provider "virtualbox" do |vb|
        vb.memory = "2048"
        vb.cpus = 2
    end

    config.vm.define "ubuntu17_10", primary: true do |ubuntu17_10|
        ubuntu17_10.vm.box = "bento/ubuntu-17.10"
        ubuntu17_10.vm.provision "shell",
            path: "scripts/provision_ubuntu17_10.sh"
    end
end
