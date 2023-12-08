# commit-msg plugin

*you should run `pip install pre-commit` first.* And add following texts in your **.pre-commit-config.yaml**

```yaml
repos:
    - repo: https://github.com/JinShultze/commit-msg-plugin
      rev: v1.0.0
      hooks:
        - id: cmmsg
```
