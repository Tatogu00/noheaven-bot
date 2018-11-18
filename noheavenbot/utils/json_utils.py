import json


class Json:

    @classmethod
    def get(cls, fp):
        with open(fp, 'r') as f:
            return json.load(f)

    @classmethod
    def make_new_index(cls, fp, content, **kw):
        file_now = cls.get(fp)
        file_now[kw.get('playlist_name')] = content
        with open(fp, 'w') as f:
            return json.dump(file_now, f, indent=1)

    @classmethod
    def add_new_value(cls, fp, index, content):
        file_now = cls.get(fp)
        file_now[index].append(content)

        with open(fp, 'w') as f:
            return json.dump(file_now, f, indent=1)