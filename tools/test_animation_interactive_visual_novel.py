import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];D=R/"chapters/pilot-001/video/interactive_visual_novel"
class TestStory(unittest.TestCase):
 def test_graph(self):
  data=json.loads((D/"story.json").read_text());nodes=data["nodes"];self.assertIn(data["start"],nodes)
  self.assertEqual(len(nodes),len(set(nodes)))
  seen=set();pending=[data["start"]]
  while pending:
   key=pending.pop()
   if key in seen:continue
   self.assertIn(key,nodes);seen.add(key);node=nodes[key]
   pending += ([node["next"]] if "next" in node else []) + [c["to"] for c in node.get("choices",[])]
  endings={nodes[k]["end"] for k in seen if "end" in nodes[k]}
  self.assertEqual(endings,{"compatibility_pact","chiplet_accord"})
  self.assertEqual(set(seen),set(nodes))
  for char in data["characters"].values():self.assertTrue((R/char["source"]).is_file());self.assertTrue((R/char["continuity"]).is_file())
 def test_source(self):
  self.assertTrue((D/"preview.html").is_file());self.assertTrue((D/"renpy/game/script.rpy").is_file())
if __name__=="__main__":unittest.main()
