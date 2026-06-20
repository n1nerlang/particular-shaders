<div align=center>
  <img src=logo/logo.png width=50%>
  <h3>Particular Shaders</h3>
  
  <br>
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&duration=3000&pause=1000&color=00A8FF&center=true&vCenter=true&width=500&lines=MCPE+1.21.30+Shader;Optimized+Performance;Stunning+Visuals" alt="Typing Animation">
  
  <br>

  <img src="https://img.shields.io/badge/Version-1.21.30-blue?style=plastic&logo=luanti&logoColor=white" alt="Version">
  <img src="https://img.shields.io/badge/RenderDragon-orange?style=plastic&logo=unity" alt="Engine">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=plastic" alt="Status">
  <img src="https://img.shields.io/badge/Version-1.1-blue?style=plastic&logo=luanti&logoColor=white" alt="Version Specific On Repo Releases">
</div>

## Shader
This is a Shader for Minecraft Bedrock 1.21.30+ using the RenderDragon engine's Deferred Technical Preview.

## How to Use
1. **Download and Install**: Download the `.mcpack` and open it with Minecraft.
2. **Enable Experiments**: When creating or editing a world, go to the **Experiments** tab and enable **Render Dragon Features for Creators**.
3. **Activate Resource Pack**: Go to **Resource Packs** and activate **Particular Shaders**.
4. **Enable Deferred Technical Preview**:
   - Enter the world.
   - Open **Settings** > **Video**.
   - Change **Graphics Mode** to **Deferred Technical Preview**.

## Features
- **Custom Lighting**: Optimized sun and moon illuminance.
- **Atmospheric Effects**: Custom sky and horizon colors with fog density.
- **Color Grading**: Enhanced contrast and saturation for a vibrant look.
- **PBR Support**: Physically Based Rendering for blocks (Metalness, Emissive, Roughness).
- **Automated Pipeline**: GitHub Actions automatically process assets and bundle the resource pack.

## Automated Asset Pipeline
This project uses an automated pipeline to process textures and generate `.texture_set.json` files for PBR support.
1. Add your base textures to `src_assets/textures/blocks/`.
2. Add your MER (Metalness, Emissive, Roughness) maps with the `_mer.png` suffix (e.g., `stone_mer.png` for `stone.png`).
3. The GitHub workflow will automatically generate the required `.texture_set.json` files and bundle the pack.
