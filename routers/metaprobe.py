from metaprobe import MetadataExtractor
import asyncio

async def MetaProbe(url):
    extractor = MetadataExtractor()
    print("hit")
    try:
      result = await extractor.get_metadata(url)
      if "title" not in result:
        return {
          "success": False,
          "error": result.get("error", "Unknown error")
        }
      return {
      "success": True,
      "metadata": result
    }
      
    except Exception as error:
      return {
        "success": False,
        "error": str(error)
    }
