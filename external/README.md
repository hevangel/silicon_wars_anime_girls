# Upstream tools

These submodules pin the default-branch commits verified when the production layout was introduced. Each upstream has its own setup.

| Path | Default branch | Commit |
| --- | --- | --- |
| `external/manga-studio` | `main` | [`2ac3cf4e3d1a`](https://github.com/ahmet360/manga-studio/commit/2ac3cf4e3d1aaec7dd39ff44498e4e8a186733c4) |
| `external/comic-pipeline` | `main` | [`24a4d658a271`](https://github.com/adachi0130/comic-pipeline/commit/24a4d658a271199832344fa31e3668e1e9e0174e) |
| `external/open-pose-costume` | `main` | [`578461c57598`](https://github.com/hongye007/open-pose-costume/commit/578461c575987ef1a4223fdac3144692d1c123e6) |
| `external/open-pose-costume-skill` | `main` | [`5004fbdb4248`](https://github.com/hongye007/open-pose-costume-skill/commit/5004fbdb42487cdfe95351b6a41ee11938b33a23) |

Initialize the smaller tools together.

```sh
git submodule update --init --depth 1 -- external/manga-studio external/comic-pipeline external/open-pose-costume-skill
```

Initialize the pose and costume reference library separately when needed. Its upstream reports about 2.5 GB of repository data, so allow for a large download and checkout.

```sh
git submodule update --init --depth 1 -- external/open-pose-costume
git submodule status
```

To upgrade a tool, fetch its upstream branch inside the submodule, inspect the target commit, and check it out. Stage that submodule path in the parent repository and include the upstream revision in the pull request. Review each upstream's setup and asset terms before using its tools or reference materials.
