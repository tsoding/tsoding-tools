let
  pkgs = import <nixpkgs> {};
  pythonBuildInputs = [ pkgs.python27Full
                        pkgs.python27Packages.virtualenv ];
  haskellBuildInputs = [ pkgs.haskellPackages.ghc
                         pkgs.haskellPackages.cabal-install
                         pkgs.haskellPackages.stack ];
in {
  tsodingToolsEnv = pkgs.stdenv.mkDerivation {
    name = "tsoding-tools";
    buildInputs = builtins.concatLists [ [ pkgs.stdenv ]
                                         pythonBuildInputs
                                         haskellBuildInputs ];
    shellHook = ''
      if [ ! -d venv ]; then
        virtualenv --python=python2.7 venv
        ./venv/bin/pip install -r requirements.txt
      fi

      source ./venv/bin/activate
    '';
    PYTHONPATH = "./commons/:./schedule/:./profiles/:./ffmpeg-edit/:./youtube/";
    SOURCE_DATE_EPOCH=315532800;
  };
}
