with import <nixpkgs> {}; {
  tsodingToolsEnv = stdenv.mkDerivation {
    name = "tsoding-tools";
    buildInputs = [ stdenv python27Full python27Packages.virtualenv ];
    shellHook = ''
      if [ ! -d venv ]; then
        virtualenv --python=python2.7 venv
        ./venv/bin/pip install -r requirements.txt
      fi
    '';
    PYTHONPATH = "./commons/:./profiles/";
  };
}
